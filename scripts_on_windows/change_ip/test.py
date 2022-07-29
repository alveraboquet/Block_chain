from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click input:has-text("百度一下")
    page.locator("input:has-text(\"百度一下\")").click()
    # expect(page).to_have_url("https://www.baidu.com/")

    # Click input[name="wd"]
    page.locator("input[name=\"wd\"]").click()

    # Go to https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=dddd&fenlei=256&rsv_pq=d470c0770006a973&rsv_t=4d2bgD85UA8lvH%2Bn%2BLpV5m3H%2B87ceeMZ%2Fyul38%2BZhafKzhWf7EDPyybcxkA&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_btype=i&prefixsug=dddd&rsp=4&inputT=5911&rsv_sug4=5911
    page.goto("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=dddd&fenlei=256&rsv_pq=d470c0770006a973&rsv_t=4d2bgD85UA8lvH%2Bn%2BLpV5m3H%2B87ceeMZ%2Fyul38%2BZhafKzhWf7EDPyybcxkA&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_btype=i&prefixsug=dddd&rsp=4&inputT=5911&rsv_sug4=5911")

    # Click input[name="wd"]
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=dddd&fenlei=256&rsv_pq=d470c0770006a973&rsv_t=4d2bgD85UA8lvH%2Bn%2BLpV5m3H%2B87ceeMZ%2Fyul38%2BZhafKzhWf7EDPyybcxkA&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_btype=i&prefixsug=dddd&rsp=4&inputT=5911&rsv_sug4=5911&rsv_jmp=fail"):
    with page.expect_navigation():
        page.locator("input[name=\"wd\"]").click()

    # Click text=百度一下
    # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=dddd&fenlei=256&oq=dddd&rsv_pq=b21661e30006e653&rsv_t=9fe7VqXx9piEiCi5qhx6FpAzVUL7r4emK%2F7bh0JLSZvvJ5w3BIW5N5uM71M&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&bs=dddd&rsv_jmp=fail"):
    with page.expect_navigation():
        page.locator("text=百度一下").click()
    # expect(page).to_have_url("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=dddd&fenlei=256&oq=dddd&rsv_pq=b21661e30006e653&rsv_t=9fe7VqXx9piEiCi5qhx6FpAzVUL7r4emK%2F7bh0JLSZvvJ5w3BIW5N5uM71M&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
