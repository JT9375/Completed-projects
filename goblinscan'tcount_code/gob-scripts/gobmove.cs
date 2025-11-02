using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;

public class gobmove : MonoBehaviour
{
    public float movespeed;
    public float jumpforce;
    private float horizontal;
    private bool isfacingright = true;
    public shootScript ShootPrefab;
    public Transform LaunchOffset;
    public float Timer = 0;
    public float Delay = 1;
    public bool Shoot = false;

    public Rigidbody2D myrigidbody;
    public Transform groundCheck;
    public LayerMask groundLayer;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //moves the rigid body left and right using 'A and D' or the left and right arrows
        horizontal = Input.GetAxisRaw("Horizontal");

        //jump
        if(Input.GetKeyDown(KeyCode.W) && Isgrounded() || Input.GetKeyDown(KeyCode.UpArrow) && Isgrounded())
        {
            myrigidbody.velocity = new Vector2(myrigidbody.velocity.x, jumpforce);
        }

        if(Timer < Delay)
        {
            Timer = Timer + Time.deltaTime;
            Shoot = false;
        }

        if(Timer > Delay)
        {
            Shoot = true;
        }

        //summons projectile
        if (Input.GetKeyDown(KeyCode.Space) && Shoot == true)
        {
            Instantiate(ShootPrefab, LaunchOffset.position, LaunchOffset.transform.rotation);
            Timer = 0;
        }

    }

    private void FixedUpdate()
    {
        //force behind the rigid body
        myrigidbody.velocity = new Vector2(horizontal * movespeed, myrigidbody.velocity.y);

        //activates the flip function
        flip();
    }

    //rotates the sprite
    private void flip()
    {
        if(isfacingright && horizontal < 0f || !isfacingright && horizontal > 0f)
        {
            isfacingright = !isfacingright;
            Vector3 localscale = transform.localScale;
            localscale.x *= -1f;
            transform.localScale = localscale;
            LaunchOffset.transform.Rotate(0, 180, 0);
        }
    }

    //Looks to see if the sprite is on the floor
    private bool Isgrounded()
    {
        return Physics2D.OverlapCircle(groundCheck.position, 0.2f, groundLayer);
    }
    
}
