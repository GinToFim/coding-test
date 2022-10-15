def solution(id_pw, db):
    db_dict = {key : value for key, value in db}
    
    _id = id_pw[0]
    pw = id_pw[1]
    
    if _id not in db_dict.keys() :
        return 'fail'
    
    if db_dict[_id] != pw :
        return 'wrong pw'
    else :
        return 'login'