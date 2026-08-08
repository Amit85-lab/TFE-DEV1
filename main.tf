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
variable "create_instance" {
  description = "Whether to create the EC2 instance"
  type        = bool
  default     = true
}


resource "aws_instance" "demo_1" {

  ami = "ami-048f4445314bcaa09"
 count = var.create_instance ? 1 : 0

  instance_type = "t3.micro"
  tags = {

    Name = "learn-terraform1"

  }


}
output "instanceid" {
  value = var.create_instance ? aws_instance.demo_1[0].id : null

}
output "instancepublicip" {
  value = var.create_instance ? aws_instance.demo_1[0].public_ip : null

}
output "instanceprivateip" {
  value = var.create_instance ? aws_instance.demo_1[0].private_ip : null

}
