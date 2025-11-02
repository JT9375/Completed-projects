using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using Unity.VisualScripting;

public class Return : MonoBehaviour
{
    public void ReturnToHome()
    {
        SceneManager.LoadScene(3);
    }
}
