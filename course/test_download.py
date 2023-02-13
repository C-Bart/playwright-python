def test_download(page):
    page.goto("https://www.jetbrains.com/pycharm/download/#section=windows")
    with page.expect_download() as download_info:
        page.locator("div:nth-child(2) > .wt-row > .wt-col_align-self_end > .wt-button_1df2673_1").first.click()
    download = download_info.value
    print(download.path())
    download.save_as("./at.txt")
