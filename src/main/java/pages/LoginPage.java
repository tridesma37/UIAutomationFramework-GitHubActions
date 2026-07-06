package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class LoginPage {

    WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    // Locator
    By txtUsername = By.id("user-name");
    By txtPassword = By.id("password");
    By btnLogin = By.id("login-button");
    By txtError = By.cssSelector("h3");

    // Action
    public void inputUsername(String username) {
        driver.findElement(txtUsername).sendKeys(username);
    }

    public void inputPassword(String password) {
        driver.findElement(txtPassword).sendKeys(password);
    }

    public void clickLogin() {
        driver.findElement(btnLogin).click();
    }

    public String getErrorMessage() {
        return driver.findElement(txtError).getText();
    }
}
