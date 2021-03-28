importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js');

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉`);
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}

const OFFLINE_URL = '{{ offline_url }}';
const appShell = [
    '/static/icons/plant.512x512.png',
    '/static/manifest.json',
    '/static/main.min.css',
    // '{{ home_url }}',
    // '{{ offline_url }}',
].map((partialUrl) => `${location.protocol}//${location.host}${partialUrl}`);

// Precache the shell.
workbox.precaching.precacheAndRoute(appShell.map(url => ({
    url,
    revision: null,
})));

// Serve the app shell from the cache.
workbox.routing.registerRoute(({ url }) => appShell.includes(url), new workbox.strategies.CacheOnly());

//Cache static external js and css
workbox.routing.registerRoute(
  ({request}) => request.destination === 'script' ||
                  request.destination === 'style',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'external-static-resources',
  })
);

//Cache dynamic images
workbox.routing.registerRoute(
    ({ request }) => request.destination === 'image',
    new workbox.strategies.CacheFirst({
        cacheName: 'dynamic-images-cache',
        plugins: [
            new workbox.cacheableResponse.CacheableResponsePlugin({
                statuses: [0, 200],
            }),
            new workbox.expiration.ExpirationPlugin({
                maxEntries: 60,
                maxAgeSeconds: 30 * 24 * 60 * 60, // 30 Days
            }),
        ],
    }),
);

// Whole page caching
// Limit the cache to 5 entries.
// TODO Stop pages in /accounts/ , /admin/ etc. from being cached. 
// workbox.routing.registerRoute(
//     ({ url }) => !appShell.includes(url) && !url.pathname.startsWith('/accounts/') && !url.pathname.startsWith('/admin/'),
//     new workbox.strategies.StaleWhileRevalidate({
//         cacheName: 'dynamic-cache',
//         plugins: [new workbox.expiration.ExpirationPlugin({
//             maxEntries: 5,
//         })],
//     })
// );

// Handle offline.
// From https://developers.google.com/web/tools/workbox/guides/advanced-recipes#provide_a_fallback_response_to_a_route
workbox.routing.setCatchHandler(({ event }) => {
    console.log(event)
    switch (event.request.method) {
        case 'GET':
            return caches.match(OFFLINE_URL);
        default:
            return Response.error();
    }
});
