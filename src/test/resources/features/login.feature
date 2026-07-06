Feature: Login Functionality

  Scenario: Login berhasil dengan username dan password yang valid
    Given User berada di halaman login
    When User memasukkan username "standard_user"
    And User memasukkan password "secret_sauce"
    And User klik tombol login
    Then User berhasil masuk ke halaman produk

  Scenario: Login gagal dengan password salah
    Given User berada di halaman login
    When User memasukkan username "standard_user"
    And User memasukkan password "salah"
    And User klik tombol login
    Then User melihat pesan error

  Scenario: Login dengan username kosong
    Given User berada di halaman login
    When User memasukkan username ""
    And User memasukkan password "secret_sauce"
    And User klik tombol login
    Then User melihat pesan error