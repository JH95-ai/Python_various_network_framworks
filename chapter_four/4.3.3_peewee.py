from peewee import *
#db=MySQLDatabase(handsomehua,**host='127.0.0.1',user='root',passwd='',charset='utf8')
db=SqliteDatabase('sampleDB.db')
class BaseModel(Model):
    class Meta:
        database=db
class Course(BaseModel):
    id=PrimaryKeyField()
    title=CharField(null=False)
    period=IntegerField()
    description=CharField()
    class Meta:
        order_by=('title',)
        db_table='course'
class Teacher(BaseModel):
    id=PrimaryKeyField()
    name=CharField(null=False)
    gender=BooleanField()
    address=CharField()
    course_id=ForeignKeyField(Course,to_field='id',related_name='course')
    class Meta:
        order_by=('name',)
        db_table='teacher'
Course.create_table()
Teacher.create_table()
Course.create(id=1,title='jingjixue')