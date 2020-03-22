from bokeh.models import CustomJS

def slider_callback_cluster(plot, source):
    # slider call back for cluster selection
    slider_callback = CustomJS(args=dict(p=plot, source=source), code="""

                var radio_value = cb_obj.value;
                var data = source.data; 

                x = data['x'];
                y = data['y'];

                x_backup = data['x_backup'];
                y_backup = data['y_backup'];

                labels = data['desc'];

                if (radio_value == '20') {
                    for (i = 0; i < x.length; i++) {
                        x[i] = x_backup[i];
                        y[i] = y_backup[i];
                    }
                }
                else {
                    for (i = 0; i < x.length; i++) {
                        if(labels[i] == radio_value) {
                            x[i] = x_backup[i];
                            y[i] = y_backup[i];
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }


            source.change.emit();
            """)
    return slider_callback

def keyword_callback_search(plot , source):
    # callback for searchbar
    keyword_callback = CustomJS(args=dict(p=plot, source=source), code="""

                var text_value = cb_obj.value;
                var data = source.data; 

                x = data['x'];
                y = data['y'];

                x_backup = data['x_backup'];
                y_backup = data['y_backup'];

                abstract = data['abstract'];
                titles = data['titles'];
                authors = data['authors'];
                journal = data['journal'];

                for (i = 0; i < x.length; i++) {
                    if(abstract[i].includes(text_value) || 
                       titles[i].includes(text_value) || 
                       authors[i].includes(text_value) || 
                       journal[i].includes(text_value)) {
                        x[i] = x_backup[i];
                        y[i] = y_backup[i];
                    } else {
                        x[i] = undefined;
                        y[i] = undefined;
                    }
                }



            source.change.emit();
            """)
    return keyword_callback