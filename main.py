from indexation.indexation import *
import click

@click.command()
@click.option('--json_file') 
def run(json_file):
    list_urls = import_json_to_list(json_file)
    list_titles = [extract_title(url) for url in list_urls]
    list_token = tokenize_list(list_titles)
    index = create_inverted_index(list_token)
    index_with_pos = create_inverted_index_with_pos(list_token)
    export_dict(index, "title.non_pos_index.json")
    export_dict(index_with_pos, "title.pos_index.json")
    export_dict(create_stats(list_token), "metadata.json")

if __name__ == '__main__':
    run()