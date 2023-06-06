def getClusters():
    return True

def getAvailableEngines(engine):
    response = client.describe_cache_engine_versions(
        Engine=engine,
        DefaultOnly=False
    )

def handler(elasticacheClient):
    response = elasticacheClient.describe_cache_clusters()
    print(response)
    # if getClusters():
    #     print('Have some clusters')
    #     elasticacheEngines = ['redis', 'memcached']
    #     for engine in elasticacheEngines:
    #         getAvailableEngines(engine)
    # else:
    #     print('Account has none Elasticache Cluster')

if __name__ == "__main__":
    handler()