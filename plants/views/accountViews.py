from django.shortcuts import render

#region Account
def profile(requests):
    # <requests> Django state
    # <return> profile.html
    
    return render(requests, 'account/profile.html')

#endregion