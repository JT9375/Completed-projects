using System.Collections;
using System.Collections.Generic;
using System.Threading;
using UnityEngine;

public class PipeSpawnScript : MonoBehaviour
{
    public GameObject pipe;
    public float spawnrate = 5;
    public float Timer = 0;
    public float HeightOffset = 5;
    public BirdScript Birdscript;
    
    void Start()
    {
        SpawnPipe();
    }

    
    void Update()
    {
        if (Timer < spawnrate) 
        {
            Timer = Timer + Time.deltaTime;
        }

        else
        {
            if(Birdscript.BirdAlive == true)
            {
                SpawnPipe();
                Timer = 0;
            }

        }
    }

    void SpawnPipe()
    {
        float Lowestpoint = transform.position.y - HeightOffset;
        float Highestpoint = transform.position.y + HeightOffset;
        Instantiate(pipe, new Vector3(transform.position.x, Random.Range(Lowestpoint, Highestpoint), 0), transform.rotation);
        
    }
}
