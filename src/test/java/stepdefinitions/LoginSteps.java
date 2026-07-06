package stepdefinitions;

import hooks.Hooks;
import io.cucumber.java.en.*;
import pages.LoginPage;

import static org.junit.Assert.assertTrue;

public class LoginSteps {

    LoginPage loginPage = new LoginPage(Hooks.driver);

    @Given("User berada di halaman login")
    public void user_berada_di_halaman_login() {
        // Browser sudah dibuka di Hooks
    }

    @When("User memasukkan username {string}")
    public void user_memasukkan_username(String username) {
        loginPage.inputUsername(username);
    }

    @And("User memasukkan password {string}")
    public void user_memasukkan_password(String password) {
        loginPage.inputPassword(password);
    }

    @And("User klik tombol login")
    public void user_klik_tombol_login() {
        loginPage.clickLogin();
    }

    @Then("User berhasil masuk ke halaman produk")
    public void user_berhasil_login() {
        assertTrue(Hooks.driver.getCurrentUrl().contains("inventory"));
    }

    @Then("User melihat pesan error")
    public void user_melihat_pesan_error() {
        assertTrue(loginPage.getErrorMessage().length() > 0);
    }
}
