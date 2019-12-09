storage "file" {
    path = "/vault/data"
  }
ui = false
listener "tcp" {
  address = "0.0.0.0:8200"
  tls_cert_file = "/vault/pki/vault.craft.htb.crt"
  tls_key_file = "/vault/pki/vault.craft.htb.key"
  tls_min_version = "tls12"
}
