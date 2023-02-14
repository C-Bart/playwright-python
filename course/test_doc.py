def test_video(browser):
    context = browser.new_context(record_video_dir="videos/")
    context.tracing.start()
    page = context.new_page()
    page.goto("")
    context.tracing.stop(path="tracing.zip")
