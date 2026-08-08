terraform {
  required_version = "1.15.8"

  cloud {
    
    organization = "TFE-DEV1"

    workspaces {
      name = "dev-cli"
    }
  }
}