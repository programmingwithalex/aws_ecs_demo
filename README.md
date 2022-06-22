# aws_ecs_demo

Copyright (c) 2021, [programmingwithalex](https://github.com/programmingwithalex)

## Description

This repo serves as a reference for the [Youtube playlist](https://www.youtube.com/watch?v=a1nnZDps_yM&list=PLbn3jWIXv_iZ566tBk_DTIPGY4fUW4qBn&index=1).

The repo covers pushing a boiler-plate Flask app to AWS ECS with the following topics covered:

* `AWS IAM (identity and access management)`
* `AWS ECR (elastic container registry)`
* `AWS ECS (elastic container service)`
* `AWS Security Groups`
* `AWS Route53`
* `Docker`
* `CI/CD with GitHub Actions`
* `AWS SSL`
* `AWS RDS (relational database storage)`
* `AWS Secrets Manager`
* `AWS EC2 Scheduled Stop/Start`
* `AWS ECS Monitoring`

## Additional Notes

`docker-compose.yml` is only for testing the application on your local machine and not in used in the AWS deployment.

## AWS Code Snippets

AWS Secrets Manager - restrict access by IAM role

```json
{
  "Version" : "2012-10-17",
  "Statement" : [ {
    "Effect" : "Deny",
    "Principal" : {
      "AWS" : "*"
    },
    "Action" : "secretsmanager:GetSecretValue",
    "Resource" : "*",
    "Condition" : {
      "StringNotLike" : {
        "aws:userid" : [ "AIDATC....", "AIDAT...." ]
      }
    }
  } ]
}
```

Additional notes:

* Access `aws:userid` with `aws-cli` and `aws iam get-user --user-name {aws-iam-user-name}`

## License

[BSD 3-Clause License](https://github.com/programmingwithalex/aws-ecs-demo/blob/main/LICENSE)
