def dismiss_none_project_files(project_file_list):
    for element in project_file_list:
        try:
            project = int(element)
        except:
            project_file_list.remove(element)
    return project_file_list
