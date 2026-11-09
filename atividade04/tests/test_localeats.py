from playwright.sync_api import sync_playwright


URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


def test_tela_de_login_permite_abrir_cadastro():
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch()
		try:
			page = browser.new_page()
			page.goto(
				f"{URL_LOCALEATS}static/login.html",
				wait_until="domcontentloaded",
			)

			campo_email_login = page.locator("#loginEmail")

			assert campo_email_login.is_visible()

			page.get_by_role("button", name="Criar Conta").click()

			assert page.locator("#regName").is_visible()
			assert page.get_by_role("button", name="Registrar").is_visible()
		finally:
			browser.close()
