# UI Automation Framework

## Deskripsi
Framework pengujian UI Website menggunakan Java, Selenium WebDriver, Cucumber, JUnit, dan Gradle.

## Teknologi
- Java
- Gradle
- Selenium WebDriver
- Cucumber
- JUnit 4
- WebDriverManager

## Struktur Project
```
src
 ├── main
 │    └── java
 │         └── pages
 └── test
      ├── java
      │     ├── hooks
      │     ├── runners
      │     └── stepdefinitions
      └── resources
            └── features
```

## Test Case
### Positive Test
- Login menggunakan username dan password yang benar.
### Negative Test
- Login menggunakan password yang salah.
### Boundary Test
- Login menggunakan username kosong.

## Cara Menjalankan
Jalankan class:

```
TestRunner.java
```

atau

```
gradle test
```

## Hasil

Framework akan menghasilkan laporan HTML pada:

```
target/cucumber-report.html
```