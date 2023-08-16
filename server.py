from flask import Flask
from flask import Flask, jsonify,request
app = Flask(__name__)


class Employee:
    def __init__(self, employee_id, name, city):
        self.employee_id = employee_id
        self.name = name
        self.city = city



# employees = {}
# employee_counter = 1

# @app.route('/greeting', methods=['GET'])
# def greeting():
#     return 'Hello world!'

# @app.route('/employee', methods=['POST'])
# def create_employee():
#     global employee_counter

#     data = request.get_json()
#     name = data.get('name')
#     city = data.get('city')

#     employee_id = str(employee_counter)
#     employees[employee_id] = {'employeeId': employee_id, 'name': name, 'city': city}
#     employee_counter += 1

#     return jsonify({'employeeId': employee_id}), 201

# @app.route('/employee/<employee_id>', methods=['GET'])
# def get_employee(employee_id):
#     employee = employees.get(employee_id)
#     if employee:
#         return jsonify(employee)
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404

# @app.route('/employees/all', methods=['GET'])
# def get_all_employees():
#     return jsonify(list(employees.values()))

# @app.route('/employee/<employee_id>', methods=['PUT'])
# def update_employee(employee_id):
#     employee = employees.get(employee_id)
#     if employee:
#         data = request.get_json()
#         employee['name'] = data.get('name', employee['name'])
#         employee['city'] = data.get('city', employee['city'])
#         return jsonify(employee), 201
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404

# @app.route('/employee/<employee_id>', methods=['DELETE'])
# def delete_employee(employee_id):
#     employee = employees.pop(employee_id, None)
#     if employee:
#         return jsonify(employee)
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404







# @app.route('/greeting', methods=['GET'])
# def greeting():
#     return 'Hello world!'

# @app.route('/employee', methods=['POST'])
# def create_employee():
#     global employee_counter

#     data = request.get_json()
#     name = data.get('name')
#     city = data.get('city')

#     employee_id = str(employee_counter)
#     employee = Employee(employee_id, name, city)
#     employees[employee_id] = employee
#     employee_counter += 1

#     return jsonify({'employeeId': employee_id}), 201

# @app.route('/employee/<employee_id>', methods=['GET'])
# def get_employee(employee_id):
#     employee = employees.get(employee_id)
#     if employee:
#         return jsonify(employee.__dict__)
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404

# @app.route('/employees/all', methods=['GET'])
# def get_all_employees():
#     employee_data = [employee.__dict__ for employee in employees.values()]
#     return jsonify(employee_data)

# @app.route('/employee/<employee_id>', methods=['PUT'])
# def update_employee(employee_id):
#     employee = employees.get(employee_id)
#     if employee:
#         data = request.get_json()
#         employee.name = data.get('name', employee.name)
#         employee.city = data.get('city', employee.city)
#         return jsonify(employee.__dict__), 201
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404

# @app.route('/employee/<employee_id>', methods=['DELETE'])
# def delete_employee(employee_id):
#     employee = employees.pop(employee_id, None)
#     if employee:
#         return jsonify(employee.__dict__)
#     else:
#         return jsonify({'message': f'Employee with {employee_id} was not found'}), 404





# class Employee:
#     def __init__(self,employeeId,name,city) -> None:
#         self.employeeId= employeeId
#         self.name= name
#         self.city=  city
    
employees={}
employee_counter=1
@app.route('/greeting',methods=['GET'])
def greetings():
    return 'Hello world!',200

@app.route('/employee',methods=['POST'])
def create_employee():
    global employee_counter
    data=request.get_json()
    #data.get('name')
    new_employee=Employee(str(employee_counter),data['name'],data['city'])
    employees[employee_counter]=new_employee
    employee_counter+=1
    response={
        "employeeId": str(employee_counter-1)
    }
    return jsonify(response),201


@app.route('/employee/<emp_id>',methods=['GET'])
def search_emp(emp_id):
    emp_id=int(emp_id)
    if emp_id in employees.keys():
        response={
            "employeeId": employees[emp_id].employeeId,
            "name": employees[emp_id].name,
            "city": employees[emp_id].city
        }
        return jsonify(response),200
    else:
        response={ 
            "message" : "Employee with "+str(emp_id)+" was not found"
        } 
        return jsonify(response),404

@app.route('/employees/all',methods=['GET'])
def all_employees():
    all_employees=[emp.__dict__ for emp in employees.values()]
    return jsonify(all_employees),200
    # for emp in employees.values():
    #     temp={
    #         "employeeId": emp.employeeId,
    #         "name": emp.name,
    #         "city": emp.city
    #     }
    #     all_employees.append(temp)
    

@app.route('/employee/<emp_id>',methods=['PUT'])
def update_emp(emp_id):
    emp_id=int(emp_id)
    if emp_id in employees.keys():
        data=request.get_json()
        employees[emp_id].name=data['name']
        employees[emp_id].city=data['city']
        response={
            "employeeId": employees[emp_id].employeeId,
            "name": employees[emp_id].name,
            "city": employees[emp_id].city
        }
        return jsonify(response),201
    else:
        response={ 
            "message" : "Employee with "+str(emp_id)+" was not found"
        } 
        return jsonify(response),404
    

@app.route('/employee/<emp_id>',methods=['DELETE'])
def delete_emp(emp_id):
    emp_id=int(emp_id)
    if emp_id in employees.keys():  
        response={
            "employeeId": employees[emp_id].employeeId,
            "name": employees[emp_id].name,
            "city": employees[emp_id].city
        }
        del employees[emp_id]
        return jsonify(response),200
    else:
        response={ 
            "message" : "Employee with "+str(emp_id)+" was not found"
        } 
        return jsonify(response),404
    















# @app.route("/calculator/greeting", methods=['GET'])
# def greeting():
#     # response = {"code":200,"content":"hello world!"}
#     # response_json = jsonify(response)
#     # response_json.data += b"\n"
#     # return response_json,200
#     return 'Hello world!'

# @app.route("/calculator/add", methods=['POST'])
# def add():
#     data = request.get_json()
#     first_number = data["first"]
#     second_number = data["second"]
#     result = first_number + second_number

#     response = {
#         "Status code": 200,
#         "result": result
#     }
#     return jsonify(response), 200

# @app.route("/calculator/add/<int:first>/<int:second>", methods=['GET'])
# def perform_addition(first, second):
#     result = first + second

#     response = {
#         "result": result
#     }
#     return jsonify(response), 200

# @app.route("/calculator/subtract", methods=['POST'])
# def subtract():
#     data=request.get_json()
#     firstnum=data["first"]
#     secondnum=data["second"]
#     result=firstnum-secondnum
#     res={
#         "Status code": 200,
#         "result": result 
#     }
#     return jsonify(res),200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
