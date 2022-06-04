

from aws_cdk import (aws_ec2 as ec2, aws_ecs as ecs,Stack,
                     aws_ecs_patterns as ecs_patterns)

from constructs import Construct

class FastAPI_Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC
        self.vpc = ec2.Vpc(self, "MyVPC", max_azs=3)

        # Create Fargate Cluster
        self.ecs_cluster = ecs.Cluster(
            self,
            "MyECSCluster",
            vpc=self.vpc,
        )

        # Create Fargate Service and ALB
        image = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=ecs.ContainerImage.from_asset(
                directory="./src",
            )
        )
        self.ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FastAPIService",
            cluster=self.ecs_cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=1,
            task_image_options=image,
        )