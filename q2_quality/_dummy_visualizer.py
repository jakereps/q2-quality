# This file is only included as an example. Remove this file when you are
# ready to develop your plugin.
import os
import os.path
import pkg_resources

import pandas as pd
import q2templates


TEMPLATES = pkg_resources.resource_filename("q2_quality", 'assets')


def mapping_viz(output_dir: str, mapping1: dict, mapping2: dict,
                key_label: str, value_label: str) -> None:
    df1 = _dict_to_dataframe(mapping1, key_label, value_label)
    df2 = _dict_to_dataframe(mapping2, key_label, value_label)

    mapping1 = df1.to_html(index=False,
                           classes='table table-striped table-hover')
    mapping1 = mapping1.replace('border="1"', 'border="0"')

    mapping2 = df2.to_html(index=False,
                           classes='table table-striped table-hover')
    mapping2 = mapping2.replace('border="1"', 'border="0"')

    index = os.path.join(TEMPLATES, 'index.html')
    context = {
        "mapping1": mapping1,
        "mapping2": mapping2
    }

    q2templates.render(index, output_dir, context=context)

def dataframe_viz(output_dir: str, table: pd.DataFrame) -> None:
    index = os.path.join(output_dir, 'index.html')
    table.to_html(open(index, 'w'))

def _dict_to_dataframe(dict_, key_label, value_label):
    return pd.DataFrame(sorted(dict_.items()),
                        columns=[key_label, value_label])
