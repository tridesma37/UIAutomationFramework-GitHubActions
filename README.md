# UI & API Automation Framework with GitHub Actions

Framework automation testing menggunakan:
- Java + Selenium WebDriver + Cucumber untuk Web UI Testing
- Python + Pytest + Requests untuk API Testing
- GitHub Actions untuk menjalankan automation test secara otomatis.

---

## Teknologi
### UI Automation
- Java 21
- Selenium WebDriver
- Cucumber
- JUnit 4
- Gradle
- WebDriverManager

### API Automation
- Python 3.14.6
- Pytest
- Requests
- Pytest HTML Report
- JsonPath-ng

### CI/CD
- GitHub Actions


---


## Project Structure
<img width="377" height="641" alt="github action" src="https://github.com/user-attachments/assets/ed205f43-1da2-4ece-ab3e-b347c422deb7" />

---


## UI Automation Test Scenarios
Automation test yang diimplementasikan:
- ✅ Positive Test – Login menggunakan username dan password yang valid.
- ✅ Negative Test – Login menggunakan password yang salah.
- ✅ Boundary Test – Login menggunakan username kosong.

## API Automation Test Scenarios
Authentication API
- ✅ Register User
- ✅ Login User
- ✅ Get User Profile
- ✅ Negative Register

Student API
- ✅ Create Student
- ✅ Get Student
- ✅ Update Student
- ✅ Delete Student

---


## UI Test Report (Cucumber)
<img width="572" height="604" alt="Cucumber Report" src="https://github.com/user-attachments/assets/6282d61a-7d47-4e1d-8141-a5617aea8d3f" />

---

## API Test Report (Pytest HTML)
<img width="1350" height="595" alt="html report" src="https://github.com/user-attachments/assets/36afd3f5-5bd1-47a6-864f-38b22b94bdc0" />

---


## GitHub Actions
Repository ini menggunakan dua workflow GitHub Actions:
- UI Automation Test
- API Automation Test
Workflow akan berjalan otomatis setiap kali terdapat push ke branch **main**.

---


## Menjalankan GitHub Actions
1. Clone repository
```bash
git clone https://github.com/tridesma37/UIAutomationFramework-GitHubActions.git
```
2. Lakukan perubahan pada project/gunakan project yang sudah ada.
3. Commit perubahan.
```bash
git add .
git commit -m "Update project"
```
4. Push ke branch `main`.
```bash
git push origin main
```
5. Buka repository di GitHub.
6. Pilih tab **Actions**.
7. Workflow akan berjalan secara otomatis.
   
## GitHub Actions Result
Workflow berhasil dijalankan menggunakan GitHub Actions
<img width="565" height="235" alt="github action result" src="https://github.com/user-attachments/assets/a7fc0e0d-034b-4385-a9d2-7daa08bfdb30" />


---

## Repository
https://github.com/tridesma37/UIAutomationFramework-GitHubActions
