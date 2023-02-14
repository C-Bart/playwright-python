def test_popup(context):
    page = context.new_page()
    page.goto("https://rrc.texas.gov/resource-center/research/gis-viewer/gis-popup-blocker-test/#")

    with page.expect_popup() as popup_info:
        page.locator("text=RUN POPUP TEST").click()

    page1 = popup_info.value
    page.wait_for_url("https://rrc.texas.gov/resource-center/research/gis-viewer/gis-popup-blocker-test/#")
    page1.close()
