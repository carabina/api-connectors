/**
 * Bybit API
 * ## REST API for the Bybit Exchange. Base URI: [https://api.bybit.com]  
 *
 * OpenAPI spec version: 0.2.10
 * Contact: support@bybit.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.math.BigDecimal;
import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

/**
 * Get Bybit OpenAPI announcements in the last 30 days in reverse order.
 **/
@ApiModel(description = "Get Bybit OpenAPI announcements in the last 30 days in reverse order.")
public class AnnouncementInfo {
  
  @SerializedName("id")
  private BigDecimal id = null;
  @SerializedName("title")
  private String title = null;
  @SerializedName("link")
  private String link = null;
  @SerializedName("summary")
  private String summary = null;
  @SerializedName("created_at")
  private String createdAt = null;

  /**
   **/
  @ApiModelProperty(value = "")
  public BigDecimal getId() {
    return id;
  }
  public void setId(BigDecimal id) {
    this.id = id;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getTitle() {
    return title;
  }
  public void setTitle(String title) {
    this.title = title;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getLink() {
    return link;
  }
  public void setLink(String link) {
    this.link = link;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getSummary() {
    return summary;
  }
  public void setSummary(String summary) {
    this.summary = summary;
  }

  /**
   **/
  @ApiModelProperty(value = "")
  public String getCreatedAt() {
    return createdAt;
  }
  public void setCreatedAt(String createdAt) {
    this.createdAt = createdAt;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AnnouncementInfo announcementInfo = (AnnouncementInfo) o;
    return (this.id == null ? announcementInfo.id == null : this.id.equals(announcementInfo.id)) &&
        (this.title == null ? announcementInfo.title == null : this.title.equals(announcementInfo.title)) &&
        (this.link == null ? announcementInfo.link == null : this.link.equals(announcementInfo.link)) &&
        (this.summary == null ? announcementInfo.summary == null : this.summary.equals(announcementInfo.summary)) &&
        (this.createdAt == null ? announcementInfo.createdAt == null : this.createdAt.equals(announcementInfo.createdAt));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.id == null ? 0: this.id.hashCode());
    result = 31 * result + (this.title == null ? 0: this.title.hashCode());
    result = 31 * result + (this.link == null ? 0: this.link.hashCode());
    result = 31 * result + (this.summary == null ? 0: this.summary.hashCode());
    result = 31 * result + (this.createdAt == null ? 0: this.createdAt.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class AnnouncementInfo {\n");
    
    sb.append("  id: ").append(id).append("\n");
    sb.append("  title: ").append(title).append("\n");
    sb.append("  link: ").append(link).append("\n");
    sb.append("  summary: ").append(summary).append("\n");
    sb.append("  createdAt: ").append(createdAt).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}