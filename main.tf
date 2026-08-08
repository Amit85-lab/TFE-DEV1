terraform {

  required_providers {

    aws = {

      source = "hashicorp/aws"

      version = "~> 5.92"

    }

  }

  required_version = "= 1.15.8"

}

provider "aws" {

  region = "ap-south-1"

}

resource "aws_instance" "demo-1" {

  ami = "ami-048f4445314bcaa09"

  instance_type = "t3.micro"
  tags = {

    Name = "learn-terraform"

  }


}
output "instanceid" {
  value = aws_instance.demo-1.id

}
output "instancepublicip" {
  value = aws_instance.demo-1.public_ip

}
output "instanceprivateip" {
  value = aws_instance.demo-1.private_ip

}