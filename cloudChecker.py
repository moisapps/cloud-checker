import boto3
import argparse

parser = argparse.ArgumentParser(description="Just an example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--profile", action="store", help="set aws credentials profile")
args = vars(parser.parse_args())
profile = args['profile']
session = boto3.Session(profile_name=profile)

def elasticache():
    import elasticache.elasticache
    elasticacheClient = session.client('elasticache')
    elasticache.elasticache.handler(elasticacheClient)

def opensearch():
    pass

def rds():
    pass

def lambda_service():
    pass

def eks():
    pass

def handler(event, context):
    elasticache()
    opensearch()
    rds()
    lambda_service()
    eks()

if __name__ == "__main__":
    handler("","")