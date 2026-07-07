# UI Automation Framework

Framework pengujian UI Website menggunakan Java, Selenium WebDriver, Cucumber, Gradle, dan JUnit.

## Teknologi
- Java
- Gradle
- Selenium WebDriver
- Cucumber
- JUnit 4
- WebDriverManager

## Project Structure
<img width="305" height="530" alt="struktur projek" src="https://github.com/user-attachments/assets/37d1ab3e-4350-47b3-966f-0c536e53c6b9" />
<img width="304" height="251" alt="struktur projek 2" src="https://github.com/user-attachments/assets/fdf4bf40-6a28-4384-a47b-d88a80a8d6c4" />

## Test Scenarios
- ✅ Positive Test – Login menggunakan username dan password yang valid.
- ✅ Negative Test – Login menggunakan password yang salah.
- ✅ Boundary Test – Login menggunakan username kosong.

## Cucumber Report
Hasil eksekusi automation testing menggunakan cucumber adalah sebagai berikut:
<img width="572" height="604" alt="cucumber report" src="https://github.com/user-attachments/assets/6282d61a-7d47-4e1d-8141-a5617aea8d3f" />


## Cara Menjalankan
1. Clone repository.
```bash
git clone https://github.com/tridesma37/UIAutomationFramework.git
```   
2. Buka project menggunakan IntelliJ IDEA.
3. Jalankan `TestRunner.java`.
4. Laporan akan tersedia di:
```text
target/cucumber-report.html
```
