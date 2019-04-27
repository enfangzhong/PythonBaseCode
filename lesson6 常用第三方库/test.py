import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c',
                        '--config',
                        default='ds_config') # # Assign config file, don't use '.py' suffix.
    parser.add_argument('-s',
                        '--spider',
                        help='',
                        default='spider_sample') # Assign spider file, don't use '.py' suffix.
    parser.add_argument('-t',
                        '--thread_count',
                        help='',
                        default=0,
                        type=int)
    return parser.parse_args()
    
if __name__ == '__main__':
    args = parse_args()
    print(args.config)
    print(args.spider)
    print(args.thread_count)