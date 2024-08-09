terraform {
  required_providers {
    aws = {
        source = "hashicorp/aws"
        version = "~>5.52.0"
    }
  }
  required_version = ">=1.8.5"
}

provider "aws" {
  region = "ap-southeast-2"
}