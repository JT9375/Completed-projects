using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class shootScript : MonoBehaviour
{
    public float speed = 10;
    public Rigidbody2D myrb;
    void Update()
    {
        transform.position += transform.right * Time.deltaTime * speed;
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        Debug.Log("projectile deleted");
        Destroy(gameObject);
    }
}
