terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.84.0"
    }
  }

  backend "s3" {
    bucket = "prakash-terraform-practice"
    key    = "terraform-expense-ecr-eks-jenkins"
    region = "us-east-1"
    dynamodb_table = "terraform-state-locking"
}
}

provider "aws" {
  # Configuration options
  region = "us-east-1"
}