# tfsec Analysis for ../../..\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf


[0m[3mResult #1[0m [0m[31mHIGH[39m[0m [1mTable encryption is not enabled.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf[2m[3m:48-68
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   48  [0m[0m[31m┌[39m[0m[0m resource[0m [38;5;37m"aws_dynamodb_table"[0m [38;5;37m"cost_recommendations"[0m {[0m
[0m[31m   49  [0m[0m[31m│[39m[0m[0m   [38;5;245mname[0m           = [38;5;37m"cost-recommendations"[0m
[0m[31m   50  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mbilling_mode[0m   = [38;5;37m"PAY_PER_REQUEST"[0m
[0m[31m   51  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mhash_key[0m       = [38;5;37m"service_name"[0m
[0m[31m   52  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mrange_key[0m      = [38;5;37m"date"[0m
[0m[31m   53  [0m[0m[31m│[39m[0m[0m [0m[0m
[0m[31m   54  [0m[0m[31m│[39m[0m[0m   attribute {[0m
[0m[31m   55  [0m[0m[31m│[39m[0m[0m     [38;5;245mname[0m = [38;5;37m"service_name"[0m
[0m[31m   56  [0m[0m[31m└[39m[0m[0m [0m    [38;5;245mtype[0m = [38;5;37m"S"[0m
[0m[90m   ..  [0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-dynamodb-enable-at-rest-encryption
[0m[0m  [2m    Impact[0m Data can be freely read if compromised
[0m[0m  [2mResolution[0m Enable encryption at rest for DAX Cluster
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/dynamodb/enable-at-rest-encryption/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dax_cluster#server_side_encryption[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #2[0m [0m[31mHIGH[39m[0m [1mIAM policy document uses sensitive action 'dynamodb:PutItem' on wildcarded resource '*'[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf[2m[3m:75
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[90m   70  [0m[0m  [38;5;33mresource[0m [38;5;37m"aws_iam_role_policy"[0m [38;5;37m"lambda_dynamodb_access"[0m {[0m
[0m[90m   ..  [0m
[0m[31m   75  [0m[0m[31m[[39m[0m[0m     [38;5;245mVersion[0m = [38;5;37m"2012-10-17"[0m,[0m
[0m[90m   ..  [0m
[0m[90m   87  [0m[0m  }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-iam-no-policy-wildcards
[0m[0m  [2m    Impact[0m Overly permissive policies may grant access to sensitive resources
[0m[0m  [2mResolution[0m Specify the exact permissions required, and to which resources they should apply instead of using wildcards.
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/iam/no-policy-wildcards/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #3[0m [0m[33mMEDIUM[39m[0m [1mPoint-in-time recovery is not enabled.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf[2m[3m:48-68
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   48  [0m[0m[31m┌[39m[0m[0m resource[0m [38;5;37m"aws_dynamodb_table"[0m [38;5;37m"cost_recommendations"[0m {[0m
[0m[31m   49  [0m[0m[31m│[39m[0m[0m   [38;5;245mname[0m           = [38;5;37m"cost-recommendations"[0m
[0m[31m   50  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mbilling_mode[0m   = [38;5;37m"PAY_PER_REQUEST"[0m
[0m[31m   51  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mhash_key[0m       = [38;5;37m"service_name"[0m
[0m[31m   52  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mrange_key[0m      = [38;5;37m"date"[0m
[0m[31m   53  [0m[0m[31m│[39m[0m[0m [0m[0m
[0m[31m   54  [0m[0m[31m│[39m[0m[0m   attribute {[0m
[0m[31m   55  [0m[0m[31m│[39m[0m[0m     [38;5;245mname[0m = [38;5;37m"service_name"[0m
[0m[31m   56  [0m[0m[31m└[39m[0m[0m [0m    [38;5;245mtype[0m = [38;5;37m"S"[0m
[0m[90m   ..  [0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-dynamodb-enable-recovery
[0m[0m  [2m    Impact[0m Accidental or malicious writes and deletes can't be rolled back
[0m[0m  [2mResolution[0m Enable point in time recovery
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/dynamodb/enable-recovery/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table#point_in_time_recovery[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #4[0m [0m[97mLOW[39m[0m [1mFunction does not have tracing enabled.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf[2m[3m:38-45
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   38  [0m[0m [0m[0m resource[0m [38;5;37m"aws_lambda_function"[0m [38;5;37m"fetch_cost_data"[0m {[0m
[0m[31m   39  [0m[0m [0m[0m   [38;5;245mfunction_name[0m = [38;5;37m"fetch-cost-data"[0m
[0m[31m   40  [0m[0m [0m[0m [0m  [38;5;245mrole[0m          = aws_iam_role.lambda_exec_role.arn[0m
[0m[31m   41  [0m[0m [0m[0m   [38;5;245mruntime[0m       = [38;5;37m"python3.9"[0m
[0m[31m   42  [0m[0m [0m[0m [0m  [38;5;245mhandler[0m       = [38;5;37m"lambda_function.lambda_handler"[0m
[0m[31m   43  [0m[0m [0m[0m [0m  [38;5;245mfilename[0m = [38;5;37m"[0m[38;5;37m${[0mpath.[38;5;33mmodule[0m[38;5;37m}[0m[38;5;37m/../src/lambda-v3.zip"[0m
[0m[31m   44  [0m[0m [0m[0m [0m[0m
[0m[31m   45  [0m[0m [0m[0m }[0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-lambda-enable-tracing
[0m[0m  [2m    Impact[0m Without full tracing enabled it is difficult to trace the flow of logs
[0m[0m  [2mResolution[0m Enable tracing
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/lambda/enable-tracing/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function#mode[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m[3mResult #5[0m [0m[97mLOW[39m[0m [1mTable encryption does not use a customer-managed KMS key.[0m [2m[0m
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────
[0m[0m  [3mc:\Users\behip\Documents\Work\IT\Cloud-Resource-Optimization-Tool\terraform\main.tf[2m[3m:48-68
[0m[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m[31m   48  [0m[0m[31m┌[39m[0m[0m resource[0m [38;5;37m"aws_dynamodb_table"[0m [38;5;37m"cost_recommendations"[0m {[0m
[0m[31m   49  [0m[0m[31m│[39m[0m[0m   [38;5;245mname[0m           = [38;5;37m"cost-recommendations"[0m
[0m[31m   50  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mbilling_mode[0m   = [38;5;37m"PAY_PER_REQUEST"[0m
[0m[31m   51  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mhash_key[0m       = [38;5;37m"service_name"[0m
[0m[31m   52  [0m[0m[31m│[39m[0m[0m [0m  [38;5;245mrange_key[0m      = [38;5;37m"date"[0m
[0m[31m   53  [0m[0m[31m│[39m[0m[0m [0m[0m
[0m[31m   54  [0m[0m[31m│[39m[0m[0m   attribute {[0m
[0m[31m   55  [0m[0m[31m│[39m[0m[0m     [38;5;245mname[0m = [38;5;37m"service_name"[0m
[0m[31m   56  [0m[0m[31m└[39m[0m[0m [0m    [38;5;245mtype[0m = [38;5;37m"S"[0m
[0m[90m   ..  [0m
[0m[90m────────────────────────────────────────────────────────────────────────────────[39m
[0m[0m  [2m        ID[0m[3m aws-dynamodb-table-customer-key
[0m[0m  [2m    Impact[0m Using AWS managed keys does not allow for fine grained control
[0m[0m  [2mResolution[0m Enable server side encryption with a customer managed key
[0m[0m
  [2mMore Information[0m[0m[0m
  [2m-[0m [34mhttps://aquasecurity.github.io/tfsec/v1.28.1/checks/aws/dynamodb/table-customer-key/[0m[0m
  [2m-[0m [34mhttps://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/dynamodb_table#server_side_encryption[0m[0m
[90m────────────────────────────────────────────────────────────────────────────────[39m


[0m[0m  [1mtimings[0m
  ──────────────────────────────────────────
[0m[0m  [2mdisk i/o            [0m 507.1µs
[0m[0m  [2mparsing             [0m 1.0113ms
[0m[0m  [2madaptation          [0m 999.1µs
[0m[0m  [2mchecks              [0m 6.5142ms
[0m[0m  [2mtotal               [0m 9.0317ms
[0m
[0m  [1mcounts[0m
  ──────────────────────────────────────────
[0m[0m  [2mmodules downloaded  [0m 0
[0m[0m  [2mmodules processed   [0m 1
[0m[0m  [2mblocks processed    [0m 6
[0m[0m  [2mfiles read          [0m 1
[0m
[0m  [1mresults[0m
  ──────────────────────────────────────────
[0m[0m  [2mpassed              [0m 6
[0m[0m  [2mignored             [0m 0
[0m[0m  [2mcritical            [0m 0
[0m[0m  [2mhigh                [0m 2
[0m[0m  [2mmedium              [0m 1
[0m[0m  [2mlow                 [0m 2
[0m
[0m  [31m[1m6 passed, 5 potential problem(s) detected.

[0m