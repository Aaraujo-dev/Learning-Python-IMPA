from vector3d import Vector3D
if __name__ == "__main__":
    vec1 = Vector3D([1, 2, 3])
    vec2 = Vector3D([4, 5, 6])
    
    print("Vec1:", vec1)
    print("Vec2:", vec2)

    sum_vec = vec1 + vec2
    print("Soma:", sum_vec)
    
    sub_vec = vec1 - vec2
    print("subtração:", sub_vec)
    
    scalar = 2
    mul_vec = vec1 * scalar
    print(f"Multiplicação por escalar ({scalar}):", mul_vec)
