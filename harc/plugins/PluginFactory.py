class PluginFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_plugin(command):
        if command == 'git:branches':
            from harc.plugins.git.GitBranches import GitBranches
            return GitBranches
        if command == 'git:release':
            from harc.plugins.git.GitRelease import GitRelease
            return GitRelease
        if command == 'pypi:deploy':
            from harc.plugins.pypi.PyPiDeploy import PyPiDeploy
            return PyPiDeploy
        if command == 'aws:eb:deploy':
            from harc.plugins.aws.AwsEbDeploy import AwsEbDeploy
            return AwsEbDeploy
        if command == 'aws:lambda:deploy':
            from harc.plugins.aws.AwsLambdaDeploy import AwsLambdaDeploy
            return AwsLambdaDeploy
        if command == 'aws:emr:deploy':
            from harc.plugins.aws.AwsEmrDeploy import AwsEmrDeploy
            return AwsEmrDeploy
        if command == 'aws:eb:deploy':
            from harc.plugins.aws.AwsEbDeploy import AwsEbDeploy
            return AwsEbDeploy
        if command == 'aws:ec2:deploy':
            from harc.plugins.aws.AwsEc2Deploy import AwsEc2Deploy
            return AwsEc2Deploy
        if command == 'docker:build':
            from harc.plugins.docker.DockerBuild import DockerBuild
            return DockerBuild
        if command == 'az:container:push':
            from harc.plugins.az.AzContainerPush import AzContainerPush
            return AzContainerPush

