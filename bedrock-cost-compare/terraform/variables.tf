variable "aws_region" {
  description = "AWS region for CloudWatch dashboard resources."
  type        = string
  default     = "us-east-1"
}

variable "dashboard_name" {
  description = "CloudWatch dashboard name."
  type        = string
  default     = "bedrock-cost-compare"
}

variable "monthly_cost_alarm_usd" {
  description = "Sample monthly cost alarm threshold in USD."
  type        = number
  default     = 100
}
