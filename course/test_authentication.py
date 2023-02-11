def test_auth(page):
    page.goto("https://github.com/login")
    page.locator("input[name='login']").click()
    page.locator("input[name='login']").fill("username")
    page.locator("input[name='password']").click()
    page.locator("input[name='password']").fill("password")
    page.locator("input:has-text('Sign in')").click()
    page.wait_for_url("https://github.com/")
