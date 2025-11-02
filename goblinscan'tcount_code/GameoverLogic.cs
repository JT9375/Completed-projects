using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class GameoverLogic : MonoBehaviour
{
    public SavedData SD;
    public Text ScoreText;

    // load and display the score when the script first begins
    void Start()
    {
        ScoreText.text = string.Format("Score: {0}", SD.Score);
    }

    public void returntomenu()
    {
        SceneManager.LoadScene(3);
    }

}
