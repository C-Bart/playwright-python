def test_visual(page, assert_snapshot):
    page.goto("")
    assert_snapshot(page.screenshot(full_page=True))
