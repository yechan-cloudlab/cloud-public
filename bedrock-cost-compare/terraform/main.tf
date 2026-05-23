terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_cloudwatch_dashboard" "bedrock_cost" {
  dashboard_name = var.dashboard_name

  dashboard_body = file("${path.module}/../dashboards/cloudwatch-dashboard.sample.json")
}

resource "aws_cloudwatch_metric_alarm" "estimated_monthly_cost" {
  alarm_name          = "${var.dashboard_name}-estimated-monthly-cost"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "EstimatedCharges"
  namespace           = "AWS/Billing"
  period              = 21600
  statistic           = "Maximum"
  threshold           = var.monthly_cost_alarm_usd
  alarm_description   = "Sample billing alarm. Billing metrics are available in us-east-1."

  dimensions = {
    Currency = "USD"
  }
}
