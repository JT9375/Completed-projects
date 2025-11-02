using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShowScore : MonoBehaviour
{
    public SavedData SD;
    public Text scoretext;
    public int currentScore;

    //Displays the score
    void Start()
    {
        currentScore = SD.Score;
        scoretext.text = currentScore.ToString();
    }


}
