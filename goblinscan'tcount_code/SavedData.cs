using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SavedData : MonoBehaviour
{
    public int Score;
    public int Health;
    public questionScript Qscript;
    public QuestionScript2 QS2;

    //collects saved data when the script is loaded at the start of each scene
    void Start()
    {
        Score = PlayerPrefs.GetInt("Score"); 
        Health = PlayerPrefs.GetInt("Health");
    }

    //Saves data whenever the function is called upon for QS1
    public void UpdateData1()
    {
        PlayerPrefs.SetInt("Score", Qscript.score);
        PlayerPrefs.SetInt("Health", Qscript.Health);
    }

    //Saves data whenever the function is called upon for QS2
    public void UpdateData2()
    {
        PlayerPrefs.SetInt("Score", QS2.score);
        PlayerPrefs.SetInt("Health", QS2.Health);
    }
}
