importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.0.0/workbox-sw.js');

if (workbox) {
    console.log(`Yay! Workbox is loaded 🎉`);
} else {
    console.log(`Boo! Workbox didn't load 😬`);
}

const OFFLINE_URL = '{{ offline_url }}';
const appShell = [
    '/static/icons/plant.512x512.png',
    '/manifest.json',
    '/static/dist/main.css',
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

//Cache js and css
workbox.routing.registerRoute(
  ({request}) => request.destination === 'script' ||
                  request.destination === 'style',
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'external-static-resources',
  })
);

//Cache images
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

// Serve the other pages from the cache and make a request to update the value in the cache.
// Limit the cache to 5 entries.
workbox.routing.registerRoute(
    ({ url }) => !appShell.includes(url),
    new workbox.strategies.StaleWhileRevalidate({
        cacheName: 'dynamic-cache',
        plugins: [new workbox.expiration.ExpirationPlugin({
            maxEntries: 5,
        })],
    })
);

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
