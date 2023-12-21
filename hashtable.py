class HashMap:

    def __init__(self, initial_capacity=40):
        self.keys = []
        self.table = [[] for _ in range(initial_capacity)]
        self.size = initial_capacity

    def hash(self,key):
        return abs(key) % self.size

    def put(self, item):
        key = item.key
        hash_value = self.hash(key)
        # print(hash_value)
        bucket_list = self.table[hash_value]
        if key not in self.keys:
            self.keys.append(key)
        #code block below will replace existing data corresponding to a key that matches put key
        for node in bucket_list:
            if node.key == key:
                node.data = item.data
                return
        bucket_list.append(item)

    def get(self, key):
        hash_value = self.hash(key)
        bucket_list = self.table[hash_value]
        for node in bucket_list:
            if node.key == key:
                return node.data
        return None

    def remove(self, key):
        hash_value = self.hash(key)
        bucket_list = self.table([hash_value])

        for node in bucket_list:
            if node.data == data:
                bucket_list.remove(node)
                break

    def get_table(self):
        return self.table

    def get_bucket(self, key):
        bucket = self.hash(key)
        return self.table[bucket]

    def keys(self):
        return self.keys()

    # def __str__(self):
    #     result = "{\n"
    #     for i, bucket_list in enumerate(self.table):
    #         result += f"  Bucket {i}: "
    #         if bucket_list:
    #             for node in bucket_list:
    #                 result += f"({node.key}: {node.data}), "
    #             result = result[:-2]  # Remove the trailing comma and space
    #         result += "\n"
    #     result += "}"
    #     return result

class Item:
    def __init__(self, key, data):
        self.key = key
        self.data = data
