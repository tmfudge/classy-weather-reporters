const Upload = () => {
    return (
      <div className="Upload" css={CSS}>
        <div className="inner">
          <div className="list">
            <h5>Your Files:</h5>
  
            <ul className="files">{/* file names here. */}</ul>
          </div>
  
          <div className="form">
            <i className="fa fa-cloud-upload fa-4x"></i>
            <p>Drag and drop files or select files below.</p>
            <button>Choose Files</button>
          </div>
        </div>
      </div>
    )
  }
  
  const CSS = css`
    height: 100%;
    width: 100%;
    background: #0d1117;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 80px;
    .inner {
      width: 100%;
      display: flex;
      justify-content: space-between;
    }
    .list {
      background-color: #121d2f;
      border: 1px solid white;
      width: 50%;
      height: 400px;
      padding: 15px;
      align-self: start;
      color: white;
      margin-right: 80px;
      ul.files {
        margin-top: 20px;
        li {
          margin-bottom: 5px;
        }
        i {
          color: #58a6ff;
          padding-left: 8px;
          cursor: pointer;
        }
      }
    }
    .form {
      background-color: #121d2f;
      width: 50%;
      padding: 15px;
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid white;
      flex-direction: column;
      margin-left: 80px;
      i,
      p {
        color: white;
      }
      button {
        background: #58a6ff;
        color: white;
        border: 1px solid white;
        padding: 2px 8px;
      }
    }