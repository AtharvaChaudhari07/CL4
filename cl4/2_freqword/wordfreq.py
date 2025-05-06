from collections import defaultdict

def map_words(line):
    return [(word,1) for word in line.strip().split()]

def sort_shuff(mapped_data):
    d = defaultdict(list)
    for word,count in mapped_data:
        d[word].append(count)

    return dict(d)

def reduce(grouped_data):
    result={}
    for word,counts in grouped_data.items():
        result[word] = sum(counts)
    return result    
    
def process_file(filename):
    mapped = []
    with open(filename,'r') as file:
        for line in file:
            mapped.extend(map_words(line))

    print("mapped data : ",mapped)        

    grouped = sort_shuff(mapped)
    print("grouped : ",grouped)

    result = reduce(grouped)
    print("result : ",result)



process_file("2_freqword\sample.txt") 
       