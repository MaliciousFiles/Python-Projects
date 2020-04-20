def validateValue(*requirements):
    def decorator(inputFunction):
        def inner(*args, **kwargs):
            answer=inputFunction(*args, **kwargs)
            checks=None
            while checks != len(requirements):
                checks=0
                for requirement in requirements:
                    try:
                        if eval(requirement):
                            checks+=1
                        else:
                            break
                    except AttributeError as attributeError:
                        raise attributeError
                if checks != len(requirements):
                    answer=inputFunction(*args, **kwargs)
                    checks=None
            return answer
        return inner
    return decorator
def getTurtleShapeBox(shapePoly):
    smallestX=shapePoly[0][0]
    greatestX=shapePoly[0][0]
    smallestY=shapePoly[0][1]
    greatestY=shapePoly[0][1]
    for point in shapePoly:
        if point[0]<smallestX:
            smallestX=point[0]
        if point[0]>greatestX:
            greatestX=point[0]
        if point[1]<smallestY:
            smallestY=point[1]
        if point[1]>greatestY:
            greatestY=point[1]
    return {"width": greatestX-smallestX, "height": greatestY-smallestY}
def openFile(filename, mode):
    try:
        return open(filename, mode=mode)
    except FileNotFoundError:
        with open(filename, mode="x") as file:
            file.close()
        return open(filename, mode=mode)
