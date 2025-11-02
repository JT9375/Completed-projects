using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PipeMoveScript : MonoBehaviour
{
    public float movespeed = 5;
    public float DeadZone = -30;


    void Start()
    {
        
    }

    
    void Update()
    {
        transform.position = transform.position + (Vector3.left * movespeed) * Time.deltaTime;

        if (transform.position.x < DeadZone)
        {
            Debug.Log("pipe destroyed");
            Destroy(gameObject);
        }
    }
}
