import gspread

def get_contacts(config_sheet,src_sheet_title,sheet_url):
    service_account = gspread.service_account(filename='service_account.json')
    sh = service_account.open_by_url(sheet_url)
    config_data = sh.worksheet(config_sheet).get_all_records()
    src_sheet = sh.worksheet(src_sheet_title)
    src_sheet_data = src_sheet.get_all_records()
    obj_list = []
    for amb in src_sheet_data:
        obj = {}
        if amb['status'] != 'completed':
            for config in config_data:
                if config['field'] != 'status':
                    obj[config['field_name']]=str(amb[config['field_name']])
            obj_list.append(obj)
    return obj_list
