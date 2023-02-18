from playwright.sync_api import expect


# def test_scrollbar(page):
#     page.goto("http://uitestingplayground.com/")
#     page.locator("text=Scrollbars").click()
#     assert page.url == "http://uitestingplayground.com/scrollbars"
#     page.locator("text=ScrollbarsAn application may use native or custom scrollbars and some elements m >> div")\
#         .nth(2).click()
#     page.mouse.wheel(100, 100)
#     expect(page.locator(".btn-primary")).to_have_text("Hidden Button")
#     page.locator(".btn-primary").click()
#
#
# def test_dynamic_table(page):
#     page.goto("http://uitestingplayground.com/")
#     page.locator("a:has-text('Dynamic Table')").click()
#     assert page.url == "http://uitestingplayground.com/dynamictable"
#     # war_var = page.locator(".bg-warning").all_inner_texts()[0].split(" ")[2]
#     war_var = page.locator(".bg-warning").inner_text().split(" ")[2]
#     table_list = page.locator("span[role='cell']")
#     print(table_list.count())


def test_progress_bar(page):
    page.goto("http://uitestingplayground.com/")
    page.locator("text=Progress Bar").click()
    assert page.url == "http://uitestingplayground.com/progressbar"
    page.locator("button:has-text('Start')").click()
    page.wait_for_selector("#progressBar[aria-valuenow='75']")
    page.locator("button:has-text('Stop')").click()
