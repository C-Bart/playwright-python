def test_frames(page):
    page.goto("url")
    page.frame_locator("...").locator("...").click()

    